# Python Tutorial

Welcome to the Python Tutorial. This guide will help you get started with Python programming on your MacBook.

## Getting Started

1. **Create a Folder for the Tutorial**
    Open your terminal and create a new folder for the tutorial:
    ```bash
    mkdir ~/Tutorial/Macbook-Python
    cd ~/Tutorial/Macbook-Python
    ```

    2. **Install Python**
        If you don't have Python installed, download and install it from the official website:
        - [Download Python](https://www.python.org/downloads/)
        ```bash
        brew install python
        ```

    3. **Install Visual Studio Code**
        Download and install Visual Studio Code (VS Code) for a powerful and lightweight code editor:
        - [Download VS Code](https://code.visualstudio.com/Download)
        ```bash
        brew install --cask visual-studio-code
        ```

        After installing, you can open VS Code from the terminal:
        ```bash
        code .
        ```


2. **Set Up a Virtual Environment**
    Create a virtual environment to manage your project dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Required Packages**
    Install any necessary packages using pip:
    ```bash
    pip install <package-name>
    ```

4. **Start Coding**
    Create a new Python file and start coding:
    ```bash
    touch main.py
    open main.py
    ```

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

Happy coding!

## Troubleshooting

### Python Installation Issues

1. **Python Command Not Found**
    If you receive a "command not found" error when trying to run Python:
    - Ensure Python is installed correctly by running:
        ```bash
        python3 --version
        ```
    - If not installed, reinstall Python using Homebrew:
        ```bash
        brew install python
        ```

2. **Pip Not Working**
    If pip is not recognized:
    - Ensure pip is installed:
        ```bash
        python3 -m ensurepip --upgrade
        ```
    - Upgrade pip to the latest version:
        ```bash
        python3 -m pip install --upgrade pip
        ```

### VS Code Installation Issues

1. **VS Code Command Not Found**
    If the `code` command is not recognized:
    - Ensure VS Code is installed correctly.
    - Install the `code` command in PATH:
        - Open VS Code, press `Cmd+Shift+P`, and type `Shell Command: Install 'code' command in PATH`.

2. **Extensions Not Installing**
    If you have trouble installing extensions:
    - Check your internet connection.
    - Try installing extensions from the command line:
        ```bash
        code --install-extension <extension-id>
        ```

3. **VS Code Not Opening**
    If VS Code does not open:
    - Try launching it from the terminal:
        ```bash
        code .
        ```
    - Reinstall VS Code if the issue persists.

For further assistance, refer to the [VS Code Documentation](https://code.visualstudio.com/docs).