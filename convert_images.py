import os
from PIL import Image

def convert_to_webp(directory):
    files = os.listdir(directory)
    extensions = ('.png', '.jpg', '.jpeg')
    
    count = 0
    for file in files:
        if file.lower().endswith(extensions):
            input_path = os.path.join(directory, file)
            name, ext = os.path.splitext(file)
            output_path = os.path.join(directory, f"{name}.webp")
            
            try:
                with Image.open(input_path) as img:
                    img.save(output_path, "WEBP", quality=80)
                    print(f"Converted: {file} -> {name}.webp")
                    count += 1
            except Exception as e:
                print(f"Failed to convert {file}: {e}")
    
    print(f"\nSuccessfully converted {count} images.")

if __name__ == "__main__":
    image_dir = "images"
    if os.path.exists(image_dir):
        convert_to_webp(image_dir)
    else:
        print(f"Directory '{image_dir}' not found.")
