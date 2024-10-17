from setuptools import setup

setup(
    name='canvas_comments',  # Your application's name
    version='1.0',  # Version number
    description='A simple GUI application to fetch comments from Canvas',  # Brief description
    py_modules=['canvas_comments'],  # Directly reference the main script
    install_requires=[  # List of required packages
        'canvasapi',  # Include all dependencies here
    ],
    entry_points={  # Defines what to run when the command is executed
        'gui_scripts': [
            'canvas_comments = canvas_comments:main',  # Refer to the main function
        ]
    },
)

