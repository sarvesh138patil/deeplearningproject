from setuptools import find_namespace_packages, setup


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements
            

setup(

name="Xray",
version="0.0.1",
author="sarvesh patil",
author_email="sarvesh138patil@gmail.com",
install_requires=get_requirements(),
package=find_packages()


)