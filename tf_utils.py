def unzipper(data_address, target_directory):
    """
    Unzips a zipped file to the target location.
    
    params:
        data_address(string): path to the zipped file
        target-directory(string): the directory insode which the contents will be extracted
    """
    import zipfile
    data = "/home/sharoonsaxena/Datasets/dogs-vs-cats.zip"
    zip_ref = zipfile.ZipFile(data, "r")
    zip_ref.extractall("/home/sharoonsaxena/Datasets/extracted/")
    zip_ref.close()
