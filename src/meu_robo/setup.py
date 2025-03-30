from setuptools import find_packages, setup

package_name = 'meu_robo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gustavo',
    maintainer_email='gustavo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = meu_robo.meu_primeiro_no:main",
            "draw_circle = meu_robo.draw_circle:main",
            "pose_subscriber = meu_robo.pose_subscriber:main",
            "controle_tartaruga = meu_robo.controle_tartaruga:main"
        ],
    },
)
