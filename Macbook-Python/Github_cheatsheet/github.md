# GitHub Cheat Sheet

## Introduction
GitHub is a web-based platform used for version control and collaborative software development. It allows users to host and review code, manage projects, and build software alongside millions of other developers. GitHub uses Git, a distributed version control system, to track changes in source code during software development.

## Creating a GitHub Repository
To upload your code to GitHub, you first need to create a repository. A repository (or "repo") is a storage space where your project lives.

### Steps to Create a Repository
1. **Sign in to GitHub**: Go to [GitHub](https://github.com) and sign in to your account.
2. **Create a new repository**:
    - Click the "+" icon in the upper-right corner and select "New repository".
    - Enter a repository name.
    - Optionally, add a description.
    - Choose to make the repository public or private.
    - Initialize the repository with a README file (optional).
    - Click "Create repository".

## Setting Up Git SSH Key and Token

### Step 1: Generate SSH Key
Generate an SSH key if you don't have one:
```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Follow the prompts to save the key. By default, it will be saved in `~/.ssh/id_rsa`.

### Step 2: Add SSH Key to GitHub
Copy the SSH key to your clipboard:
```sh
cat ~/.ssh/id_rsa.pub
```
Go to GitHub:
- Click on your profile picture in the upper-right corner and select `Settings`.
- In the left sidebar, click `SSH and GPG keys`.
- Click `New SSH key`, provide a title, and paste your key into the "Key" field.
- Click `Add SSH key`.

### Step 3: Create a Personal Access Token
Go to GitHub:
- Click on your profile picture in the upper-right corner and select `Settings`.
- In the left sidebar, click `Developer settings`.
- Click `Personal access tokens`, then `Generate new token`.
- Select the scopes or permissions you'd like to grant this token.
- Click `Generate token` and copy the token.

## Uploading Code from Terminal

### Example to update github repository
```bash
echo "# PyFizik" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/collegephysicsonline/PyFizik.git
git push -u origin main

```

### Step 1: Install Git
Ensure Git is installed on your system. You can download it from [git-scm.com](https://git-scm.com/).

### Step 2: Clone the Repository
Clone the repository to your local machine:
```sh
git clone git@github.com:your-username/your-repository.git
```

### Step 3: Add Your Code
Navigate to the repository directory and add your code files:
```sh
cd your-repository
# Add your files to the repository directory
```

### Step 4: Commit Changes
Stage and commit your changes:
```sh
git add .
git commit -m "Initial commit"
```

### Step 5: Push to GitHub
Push your changes to the remote repository:
```sh
git push origin main
```

## Uploading Code from VS Code

### Step 1: Install Git and VS Code
Ensure Git and Visual Studio Code (VS Code) are installed on your system.

### Step 2: Open Repository in VS Code
Open your repository in VS Code:
- Open VS Code.
- Go to `File > Open Folder` and select your repository folder.

### Step 3: Add Your Code
Add your code files to the repository folder.

### Step 4: Commit Changes
Use the Source Control feature in VS Code:
- Click the Source Control icon in the Activity Bar on the side of the window.
- Stage your changes by clicking the "+" icon next to the files.
- Enter a commit message in the message box and click the checkmark icon to commit.

### Step 5: Push to GitHub
Push your changes to the remote repository:
- Click the "..." icon in the Source Control panel.
- Select `Push` from the dropdown menu.

## Example: Uploading Code to GitHub

### Step-by-Step Example
1. **Create a repository on GitHub**:
    - Repository name: `example-repo`
    - Description: `Example repository for tutorial`
    - Public repository
    - Initialize with a README

2. **Clone the repository**:
    ```sh
    git clone git@github.com:your-username/example-repo.git
    ```

3. **Add code files**:
    ```sh
    cd example-repo
    echo "# Example Project" > README.md
    ```

4. **Commit changes**:
    ```sh
    git add README.md
    git commit -m "Add README file"
    ```

5. **Push to GitHub**:
    ```sh
    git push origin main
    ```

By following these steps, you can easily upload your code to GitHub using either the terminal or VS Code. Happy coding!