from setuptools import setup

setup(
    name="grpc_madmin",
    version="0.6",
    packages=["grpc_madmin"],
    install_requires=["grpcio", "googleapis-common-protos"],
    zip_safe=False,
)
