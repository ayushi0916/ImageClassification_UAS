def RGB_Image_To_Readable(folder_path_add,output_folder_add):
  # Folder path containing the TIFF files
  folder_path = "/content/drive/MyDrive/7. SaltMUAS_share/UAS Data Collection/North River/Orthos and DEMs 2022/21Jun2022/High/299x299 Mica tif Tiles"

  # Output folder for normalized images
  output_folder = '/content/drive/MyDrive/RGB_21Jun_High_NOR'

  # Create the output folder if it doesn't exist
  os.makedirs(output_folder, exist_ok=True)

  i=0

  # Process each TIFF file in the folder
  for filename in os.listdir(folder_path):
    try:
      if filename.endswith('.tif'):
          # Load the TIFF file
          tiff_path = os.path.join(folder_path, filename)
          tiff_data = tifffile.imread(tiff_path)

          # Normalize the pixel values to the range of [0, 1]
          tiff_data_normalized = tiff_data.astype(np.float32) / np.max(tiff_data)

          # Create a PIL Image from the normalized data
          image = Image.fromarray((tiff_data_normalized * 255).astype(np.uint8))

          # Save the normalized image
          output_path = os.path.join(output_folder, filename)
          image.save(output_path)



          print(f"Image '{filename}' saved successfully!")

          i=i+1


    except:
      print(f"Skipping file {filename} due to error")
      continue
  print(i)
  
def Augment_data(input_folder_1_link,input_folder_2_link,input_folder_3_link,output_dir1_link,output_dir2_link,output_dir3_link):
  input_folder_1 = input_folder_1_link
  input_folder_2 = input_folder_2_link
  input_folder_3 = input_folder_3_link

  output_dir_regular = output_dir1_link
  output_dir_irregular = output_dir2_link
  output_dir_other = output_dir3_link


  # Create the output directories if they don't exist
  if not os.path.exists(output_dir_regular):
    os.makedirs(output_dir_regular)
  if not os.path.exists(output_dir_irregular):
    os.makedirs(output_dir_irregular)
  if not os.path.exists(output_dir_other):
    os.makedirs(output_dir_other)

  # Define the augmentations
  transform = A.Compose([    A.HorizontalFlip(p=1),    A.VerticalFlip(p=1)])

  # Process input folder 1
  i = 0
  for image_file in os.listdir(input_folder_1):
      image_path = os.path.join(input_folder_1, image_file)
      image = tifffile.imread(image_path)
      augmented = transform(image=image)
      image_1 = augmented["image"]  # Original image
      image_2 = np.fliplr(image_1)  # Flipped horizontally
      image_3 = np.flipud(image_1)  # Flipped vertically
      image_4 = np.flipud(image_2)  # Flipped both horizontally and vertically
      # Save the four distinct images in output folder 1
      cv2.imwrite(os.path.join(output_dir_regular, str(i) + '_' + image_file), image_1)
      cv2.imwrite(os.path.join(output_dir_regular, str(i) + '_'  + "hflip_" + image_file), image_2)
      cv2.imwrite(os.path.join(output_dir_regular, str(i) + '_' + "vflip_" + image_file), image_3)
      cv2.imwrite(os.path.join(output_dir_regular, str(i) + '_' + "hvflip_" + image_file), image_4)
      i = i + 1

  # Process input folder 2
  i = 0
  for image_file in os.listdir(input_folder_2):

      image_path = os.path.join(input_folder_2, image_file)
      image = tifffile.imread(image_path)
      augmented = transform(image=image)
      image_1 = augmented["image"]  # Original image
      image_2 = np.fliplr(image_1)  # Flipped horizontally
      image_3 = np.flipud(image_1)  # Flipped vertically
      image_4 = np.flipud(image_2)  # Flipped both horizontally and vertically
      # Save the four distinct images in output folder 2
      cv2.imwrite(os.path.join(output_dir_irregular, str(i) + '_' + image_file), image_1)
      cv2.imwrite(os.path.join(output_dir_irregular, str(i) + '_'  + "hflip_" + image_file), image_2)
      cv2.imwrite(os.path.join(output_dir_irregular, str(i) + '_' + "vflip_" + image_file), image_3)
      cv2.imwrite(os.path.join(output_dir_irregular, str(i) + '_' + "hvflip_" + image_file), image_4)
      i = i + 1



  # Process input folder 3
  i = 0
  for image_file in os.listdir(input_folder_3):

      image_path = os.path.join(input_folder_3, image_file)
      image = tifffile.imread(image_path)
      augmented = transform(image=image)
      image_1 = augmented["image"]  # Original image
      image_2 = np.fliplr(image_1)  # Flipped horizontally
      image_3 = np.flipud(image_1)  # Flipped vertically
      image_4 = np.flipud(image_2)  # Flipped both horizontally and vertically
      # Save the four distinct images in output folder 2
      cv2.imwrite(os.path.join(output_dir_other, str(i) + '_' + image_file), image_1)
      cv2.imwrite(os.path.join(output_dir_other, str(i) + '_'  + "hflip_" + image_file), image_2)
      cv2.imwrite(os.path.join(output_dir_other, str(i) + '_' + "vflip_" + image_file), image_3)
      cv2.imwrite(os.path.join(output_dir_other, str(i) + '_' + "hvflip_" + image_file), image_4)
      i = i + 1

