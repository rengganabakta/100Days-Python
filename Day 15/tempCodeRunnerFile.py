        IsEnoughIngredients = check_resource(coffee)
        if IsEnoughIngredients == True:
            IsEnoughMoney, user_money = check_money(coffee)
            # if IsEnoughMoney == True:
            #     proceded()