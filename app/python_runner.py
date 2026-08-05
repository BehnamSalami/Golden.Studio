def run_code(code, financial_data):

    try:

        local = {}

        exec(code,{},local)


        if "analyze" in local:

            result = local["analyze"](financial_data)

            return str(result)


        return "تابع analyze در کد پروژه پیدا نشد"



    except Exception as e:

        return "خطا در تحلیل:\n" + str(e)