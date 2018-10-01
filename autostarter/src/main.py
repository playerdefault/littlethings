import click, sys
from subprocess import Popen

@click.command()
@click.option('--programs', '-p', multiple=True)
def starter(programs):
    program_paths = []
    
    # check the programs
    for program in programs:
        if (program == 'vs'):
            program_paths.append(r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE\devenv.exe')
        elif (program == 'nppp'):
            program_paths.append(r'C:\Program Files\Notepad++\notepad++.exe')
        elif (program == 'ssms'):
            program_paths.append(r'C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\ManagementStudio\Ssms.exe')
        elif (program == 'firefox'):
            program_paths.append(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        elif (programs == {'all'} ):
            program_paths.append(r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE\devenv.exe')
            program_paths.append(r'C:\Program Files\Notepad++\notepad++.exe')
            program_paths.append(r'C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\ManagementStudio\Ssms.exe')
            program_paths.append(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    
    # launch the programs
    for program_path in program_paths:
        Popen(program_path)

if __name__ == "__main__":
    starter()
    sys.exit()