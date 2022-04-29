# Python GoogleSheetsAPI-imports
from googleapiclient.discovery import build
from google.oauth2 import service_account



class GoogleApi:

    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    my_credentials = None
    my_credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1dAFFThOXIuM-YKtKMEzSgHaD0HPpFLsUamiMZhlrOOk'

    service = build('sheets', 'v4', credentials=my_credentials)

    # Call the Sheets API
    mydata = [["8/1/2020","Joe3","MidWest","IL","New Brand",563.65,342.45]]


    def appendToActCampAutomationsSheet(self, data):
        request = self.service.spreadsheets().values().append(
                spreadsheetId=self.SAMPLE_SPREADSHEET_ID, 
                range="ActCampAutomationsSheet!A2", # where to start from in searching for the first empty row
                valueInputOption="USER_ENTERED", #how the input data should be interepreted. Either a)RAW (will not be parsed) or b)USER_ENTERED (ie. strings may be converted to nubmers, dates, etc)
                insertDataOption="INSERT_ROWS", #how the input data should be inserted. Either a) OVERWRITE or b)INSERT_ROWS
                body={"values":data} #
        )

        request.execute()
        return None


    # The method bellow generates the following list with sublists
    # [
    #     [ 'D1','E1','F1','G1','H1','I1' ], 
    #     [ 'D2','E2','F2','G2','H2','I2' ],
    #     ...
    #     [ 'D1300','E1300','F1300','G1300','H1300','I1300']
    # ]
    @property
    def target_cells(self):
        href_cells_list = []
        target_columns = ['D', 'E', 'F', 'G', 'H', 'I']
        target_lines = [*range(2, 1301, 1)]

        for line_idx, line_elmnt in enumerate(target_lines):
                intermediary_list = []
                href_cells_list.append(intermediary_list)
                for col_idx, col_elmnt in enumerate(target_columns):
                        # print(str(target_lines[line_idx]) + target_columns[col_idx])
                        intermediary_list.append( target_columns[col_idx] + str(target_lines[line_idx]) )
        
        return href_cells_list

