        sheet = workbook["Soft Tissue-Guided"]

        # Column B = English
        # Column E = Bulgarian

        excel_strings = {}

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):
            if len(row) < 5:
                continue

            english_value = row[1]   # Column B
            bulgarian_value = row[2] # Column E

            if bulgarian_value is None:
                continue

            english = (
                str(english_value).strip()
                if english_value is not None
                else ""
            )

            bulgarian = str(bulgarian_value).strip()

            if ignore_text(bulgarian):
                continue

            key = normalize(bulgarian)

            if key not in excel_strings:
                excel_strings[key] = []

            excel_strings[key].append(english)