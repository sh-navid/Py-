import re
import os


class File:
    def find(filename, path='.'):
        for root, dirs, files in os.walk(path):
            if filename in files:
                return os.path.join(root, filename)
        return None
    

    


class DynamicImport:
    @staticmethod
    def exec(content):
        matches = re.findall(r"with +(.*) +import +(.*)", content)

        for match in matches:
            (module, imports) = match
            print(module, imports)

            result = File.find(f'{module}.py')
            if not result:
                ImportError("Cannot find module '{module}'")

                


    


class Compiler:
    @staticmethod
    def compile_pyp(path):
        print(path)

        with open(path, "r") as f:
            content = f.read()

        DynamicImport.exec(content)
