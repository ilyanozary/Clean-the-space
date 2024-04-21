import os
import shutil

def organize_music_files(source_folder, destination_folder):
    """
    Organizes music files (based on specified extensions) from a source folder into a destination folder.
    
    Args:
        source_folder (str): Path to the source folder containing music files.
        destination_folder (str): Path to the destination folder for organized music files.
    """
    music_extensions = ['.mp3', '.wav', '.ogg', '.flac']

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if any(filename.endswith(ext) for ext in music_extensions):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to music folder.")

def organize_document_files(source_folder, destination_folder):
    """
    Organizes document files (based on specified extensions) from a source folder into a destination folder.
    
    Args:
        source_folder (str): Path to the source folder containing document files.
        destination_folder (str): Path to the destination folder for organized document files.
    """
    doc_extensions = ['.doc', '.docx', '.pdf', '.txt', '.pptx']

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if any(filename.endswith(ext) for ext in doc_extensions):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to documents folder.")

def organize_image_files(source_folder, destination_folder):
    """
    Organizes image files (based on specified extensions) from a source folder into a destination folder.
    
    Args:
        source_folder (str): Path to the source folder containing image files.
        destination_folder (str): Path to the destination folder for organized image files.
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if any(filename.endswith(ext) for ext in image_extensions):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to images folder.")

# Get input from user for source and destination paths
source_folder_music = input("Enter the path to the source folder containing music files: ")
destination_folder_music = input("Enter the path to the destination folder for music files: ")

source_folder_docs = input("Enter the path to the source folder containing document files: ")
destination_folder_docs = input("Enter the path to the destination folder for document files: ")

source_folder_images = input("Enter the path to the source folder containing image files: ")
destination_folder_images = input("Enter the path to the destination folder for image files: ")

# Organize files using user-provided paths
organize_music_files(source_folder_music, destination_folder_music)
organize_document_files(source_folder_docs, destination_folder_docs)
organize_image_files(source_folder_images, destination_folder_images)


