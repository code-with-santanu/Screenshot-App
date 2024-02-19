import os
from pathlib import Path


def createStoragePath():

    user_home_dir = Path.home()
    print("Home Directory = ", user_home_dir)

    try:
        onedrive_path = user_home_dir / "OneDrive" / "Pictures" / "Screenshots"
        if (os.path.exists(onedrive_path)):
            required_path = onedrive_path
            print("Onedrive Path already exists: ", onedrive_path)

        else:
            user_Pic_dir = user_home_dir / "Pictures"
            other_dir = user_Pic_dir / "Screenshots"
            if (os.path.exists(other_dir)):
                print("Path already exists: ", other_dir)

            else:
                mode = 0o777
                os.makedirs(other_dir, mode)
                print("Folder created succesfully")

            required_path = other_dir

    except Exception as e:
        print(e)
    finally:

        print("Final Path = ", required_path)

    return required_path


if __name__ == "__main__":
    createStoragePath()
