from distutils.core import setup, Extension

module = Extension(
    'pyvicon_module',
    sources=['pyvicon/pyvicon.cpp'],
    libraries=['ViconDataStreamSDK_CPP'],
    # extra_compile_args=["-isysroot/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/"] #,"-L/Users/florian/Downloads/ViconDataStreamSDK_1.8.0_105615h/Mac","-lViconDataStreamSDK_CPP","-L."],
)

setup(
    name='pyvicon',
    version='0.2',
    description='Python wrapper over Vicon DataStream SDK, works with v1.7.1',
    license='GPL-3.0',
    author='Mathieu Garon',
    author_email='mathieugaron91@gmail.com',
    packages=['pyvicon'],
    ext_modules=[module],
    install_requires=['gym', 'numpy'])
