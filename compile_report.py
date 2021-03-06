import yaml
import shlex
import subprocess


log_dir = "./logs/"
emoji = {True: ":+1:",
         False: ":x:",
         None: ":bangbang:"}


def compile_main_report():
    packages = yaml.load(open('packages_data.yaml', 'r'))

    report_lines = ["|package|package availalbe|availability type|",
                    "|-------|:----------------|:-----------------|"]

    for package in packages:
        # We should probably seperate Not tried and tried and failed cases
        report = "|%s|%s|%s|" % (package,
                                 emoji[packages[package]['package_available']],
                                 packages[package]['availability_type'])

        report_lines.append(report)

    # Score
    N = len(packages)
    num_available_packages = sum([1 for package in packages if
                                  packages[package]['package_available']])
    report_lines.append("\nPackages Available: %s/%s" % (num_available_packages, N))

    anaconda = sum([1 for package in packages if
                    packages[package]['availability_type'] == 'Anaconda'])
    report_lines.append("\nAnaconda: %s/%s" % (anaconda, N))

    conda_build = sum([1 for package in packages if
                       packages[package]['availability_type'] == 'conda-build'])
    report_lines.append("\nconda build: %s/%s" % (conda_build, N))

    pipbuild = sum([1 for package in packages if
                    packages[package]['availability_type'] == 'pipbuild'])
    report_lines.append("\npipbuild: %s/%s" % (pipbuild, N))

    open("main_report.md", "w").writelines("\n".join(report_lines))
    cmd = "grip main_report.md --export"
    subprocess.call(shlex.split(cmd))


def compile_recipe_report():
    recipes = yaml.load(open('recipes_data.yaml', 'r'))

    report_lines = ["|package|recipe available|error type|",
                    "|-------|:---------------|:---------|"]

    for package in recipes:
        # We should probably seperate Not tried and tried and failed cases
        log_file = log_dir + "%s_recipe.log" % package
        report = "|%s|%s|[%s](%s)|" % (package,
                                       emoji[recipes[package]['recipe_available']],
                                       recipes[package].setdefault('error_type', None),
                                       log_file)

        report_lines.append(report)

    # Score
    N = len(recipes)
    num_available_recipes = sum([1 for package in recipes
                                 if recipes[package]['recipe_available']])
    report_lines.append("\nSuccessful recipes: %s/%s" % (num_available_recipes, N))

    num_failed_recipes = sum([1 for package in recipes
                             if recipes[package]['recipe_available'] is False])
    report_lines.append("\nFailed Recipes:%s/%s" % (num_failed_recipes, N))

    open("recipe_report.md", "w").writelines("\n".join(report_lines))
    cmd = "grip recipe_report.md --export"
    subprocess.call(shlex.split(cmd))


def compile_build_report():
    build = yaml.load(open('build_data.yaml', 'r'))

    report_lines = ["|package|build successful|error type|",
                    "|-------|:---------------|:---------|"]

    for package in build:
        # We should probably seperate Not tried and tried and failed cases
        log_file = log_dir + "%s_build.log" % package
        report = "|%s|%s|[%s](%s)|" % (package,
                                       emoji[build[package]['build_successful']],
                                       build[package].setdefault('error_type', None),
                                       log_file)

        report_lines.append(report)

    # Score
    N = len(build)
    num_available_build = sum([1 for package in build
                               if build[package]['build_successful']])
    report_lines.append("\nSuccesful builds : %s/%s" % (num_available_build, N))

    num_failed_build = sum([1 for package in build
                            if build[package]['build_successful'] is False])
    report_lines.append("\nFailed Builds: %s/%s" % (num_failed_build, N))

    open("build_report.md", "w").writelines("\n".join(report_lines))
    cmd = "grip build_report.md --export"
    subprocess.call(shlex.split(cmd))


def compile_pipbuild_report():
    pipbuild = yaml.load(open('pipbuild_data.yaml', 'r'))

    report_lines = ["|package|pipbuild successful|error type|",
                    "|-------|:------------------|:---------|"]

    for package in pipbuild:
        # We should probably seperate Not tried and tried and failed cases
        log_file = log_dir + "%s_pipbuild.log" % package
        report = "|%s|%s|[%s](%s)|" % (package,
                                       emoji[pipbuild[package]['pipbuild_successful']],
                                       pipbuild[package].setdefault('error_type', None),
                                       log_file)

        report_lines.append(report)

    # Score
    N = len(pipbuild)
    num_available_pipbuild = sum([1 for package in pipbuild
                                  if pipbuild[package]['pipbuild_successful']])
    report_lines.append("\nSuccesful pipbuilds : %s/%s" % (num_available_pipbuild, N))

    num_failed_pipbuild = sum([1 for package in pipbuild
                               if pipbuild[package]['pipbuild_successful'] is False])
    report_lines.append("\nFailed Builds: %s/%s" % (num_failed_pipbuild, N))

    open("pipbuild_report.md", "w").writelines("\n".join(report_lines))
    cmd = "grip pipbuild_report.md --export"
    subprocess.call(shlex.split(cmd))


def main():
    compile_main_report()
    compile_recipe_report()
    compile_build_report()
    compile_pipbuild_report()


if __name__ == "__main__":
    main()
