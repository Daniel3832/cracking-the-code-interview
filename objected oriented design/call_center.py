class callCenter:
    dispatchCall(employee):
        if employee == respondent:
            return Respondent()
        if employee == manager:
            return Manager()
        elif employee == director:
            return Director()
        return None

    getCall():
        return dispatchCall()