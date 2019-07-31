from setuptools import setup

setup(name='searchyption',
        version='0.1',
        description='Searchable Encryption',
        url='https://gitlab.com/farshad-nejati/searchyption.git',
        author='Farshad Nejati',
        author_email='nejati.farshad93@gmail.com',
        license='MIT',
        packages=['searchyption'],
        install_requires=[
            'PyPDF2',
            'python-docx',
            'nltk',
            # 'hazm',
        ],
        entry_points = {
            'console_scripts': ['searchyption=searchyption.command_line:main'],
        },
        zip_safe=False)
      
    #   dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
    
        # scripts=['bin/searchyption-joke'],