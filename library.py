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
