# 📥 SFC Downloader

A small Python script for downloading all the videos in an SFC course.

## Overview

**SFC Downloader** is a Python script designed to help users download all videos from an SFC course efficiently. Using Selenium, the tool automates the process of navigating the course pages and downloading the videos, saving you time and ensuring you have offline access to your course materials.

## Features

- **Batch Download**: Download all videos from a specified SFC course in one go.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Required Python packages (see below for installation).
- [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ahmosys/sfc-downloader.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd sfc-downloader
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download and set up ChromeDriver**:

    - Download the ChromeDriver that matches your Google Chrome version from [here](https://sites.google.com/chromium.org/driver/).
    - Make sure the ChromeDriver executable is in your system's PATH or place it in the same directory as your script.

## Usage

1. **Create a `.env` file**:

    Create a `.env` file in the project directory and add your SFC login credentials:

    ```env
    SYMFONYCASTS_USERNAME=your_username
    SYMFONYCASTS_PASSWORD=your_password
    ```

2. **Update the `BASE_URL` in `main.py`**:

    Open `main.py` and replace the `BASE_URL` variable with the URL of the course you want to download:

    ```python
    BASE_URL = "https://sfc.example.com/course-url"
    ```

3. **Run the script**:

    ```bash
    python main.py
    ```
The script will use Selenium to navigate to the specified course URL, log in with your credentials, and start downloading all the videos.

## Contributing

We welcome contributions! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

### General Contribution Steps

1. **Fork the project**.
2. **Create a new feature branch** (`git checkout -b feature/your-feature`).
3. **Commit your changes** (`git commit -m 'Add a feature'`).
4. **Push to your branch** (`git push origin feature/your-feature`).
5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
