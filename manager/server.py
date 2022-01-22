REGISTERED_PACKAGES = 'registered'
INSTALLED_PACKAGES = 'installed'

PACKAGES = {
    REGISTERED_PACKAGES: dict(),
    INSTALLED_PACKAGES: list()
}


def _process_input(input_line):
    command, *args = input_line.split(' ')

    if command.upper() == 'DEPEND':
        if not args:
            return

        package_name = args[0]
        
        dependecies = args[1:] if len(args) > 1 else []
        dependecies = [dependency.lower() for dependency in dependecies]
        
        PACKAGES.get(REGISTERED_PACKAGES).update({
            package_name.lower(): dependecies
        })

    elif command.upper() == 'INSTALL':
        if not args:
            return

        package_name = args[0]
        package_name = package_name.lower()

        registed_packages = PACKAGES.get(REGISTERED_PACKAGES)
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)

        if package_name in installed_packages:
            print('Package already installed')
            return

        if package_name not in registed_packages:
            print('Package not found')
            return
        
        dependecies = registed_packages.get(package_name)

        installed_packages.append(package_name)

        for dependency in dependecies:
            if dependency not in installed_packages:
                installed_packages.append(dependency)

    elif command.upper() == 'REMOVE':
        if not args:
            return

        package_name = args[0]
        package_name = package_name.lower()

        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        registed_packages = PACKAGES.get(REGISTERED_PACKAGES)

        if package_name not in installed_packages:
            print('Package is not installed')
            return

        installed_packages.remove(package_name)

        dependecies = registed_packages.get(package_name)
        dependencies_in_use = list()
        for dependency in dependecies:
            for installed_package in installed_packages:
                if dependency in registed_packages.get(installed_package, []):
                    dependencies_in_use.append(dependency)

            if dependency in dependencies_in_use:
                continue

            installed_packages.remove(dependency)

    elif command.upper() == 'LIST':
        installed_packages = PACKAGES.get(INSTALLED_PACKAGES)
        print('\n'.join(installed_packages))


    return command.upper() == 'END'


def start_package_server():
    print('Package manager started.')
    print('Listening for commands...')

    while True:
        line = input()

        terminate = _process_input(line)

        if terminate:
            break
