import os
from PIL import Image

class LetterCropper:
    def __init__(self, input_dir, output_dir, target_width, target_height):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.target_width = target_width
        self.target_height = target_height

    def crop_letters(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for filename in os.listdir(self.input_dir):
            if filename.endswith('.png'):
                image_path = os.path.join(self.input_dir, filename)
                output_path = os.path.join(self.output_dir, filename)

                try:
                    image = Image.open(image_path)
                    cropped_image = self.crop_to_target_size(image)
                    cropped_image.save(output_path)
                    print(f"Processed: {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    def crop_to_target_size(self, image):
        width, height = image.size

        left = 0
        top = 14
        right = width
        bottom = height - 14

        cropped_image = image.crop((left, top, right, bottom))
        cropped_image = cropped_image.resize((self.target_width, self.target_height), Image.ANTIALIAS)

        return cropped_image

def main():
    input_dir = 'letters'
    output_dir = 'out'
    target_width = 116
    target_height = 116

    cropper = LetterCropper(input_dir, output_dir, target_width, target_height)
    cropper.crop_letters()

if __name__ == "__main__":
    main()