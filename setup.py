import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="mars-rover-dru1208",
	version="0.0.1",
	author="Andrew",
	author_email="andrewhsieh1208@gmail.com",
	description="Mars Rover Python Implementation",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/dru1208/mars_rover_python",
	packages=setuptools.find_packages(),
	classifiers=(
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	),
	python_requires=">=3.6",
)

