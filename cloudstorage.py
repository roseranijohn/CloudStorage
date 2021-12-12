import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.A94VjsNzA2DeOiWFxNYlR2OUTrkmzm8kHqgdmAXU4HROLSTDbEVWAP6gOQN2ptUkudqXY1cuAHwjFIk72NzDueM6G2CUhtO0yMm8vBqAmz_DWWPcvNS85SBnGq5ACEMZ89Wrejw'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = "/PythonTest/trial.pdf"

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()