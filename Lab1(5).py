def unlist(nums, res = []):

    for num in nums:
        if type(num) == list:
            unlist(num)
        else:
            res.append(num)

    return res

