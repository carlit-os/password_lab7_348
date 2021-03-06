import common


def dot_prod(weight, feature):
    result = sum(x_i * y_i for x_i, y_i in zip(weight, feature))
    if result >= 0:
        return True
    else:
        return False


def vec_sub(weight, feature):
    return [a_i - b_i for a_i, b_i in zip(weight, feature)]


def vec_add(weight, feature):
    return [a_i + b_i for a_i, b_i in zip(weight, feature)]


def part_one_classifier(data_train, data_test):
    # PUT YOUR CODE HERE
    # Access the training data using "data_train[i][j]"
    # Training data contains 3 cols per row: X in
    # index 0, Y in index 1 and Class in index 2
    # Access the test data using "data_test[i][j]"
    # Test data contains 2 cols per row: X in
    # index 0 and Y in index 1, and a blank space in index 2
    # to be filled with class
    # The class value could be a 0 or a 1
    weight = [0, 0, 0]
    incorrect = 1
    counter = 0
    while incorrect > 0:
        counter += 1
        incorrect = 0
        for data in data_train:
            feature = [data[0], data[1], 1]
            prediction = dot_prod(weight, feature)
            if prediction != data[2]:
                incorrect += 1
                if prediction:
                    weight = vec_sub(weight, feature)
                else:
                    weight = vec_add(weight, feature)

    for data in data_test:
        data[2] = dot_prod(weight, [data[0], data[1], 1])
    return


def arg_max(weights, feature):
    result = []
    for weight in weights:
        result.append(sum(x_i * y_i for x_i, y_i in zip(weight, feature)))

    return result.index(max(result))


def scale(feature, rate):
    return [rate * i for i in feature]


def part_two_classifier(data_train, data_test):
    # PUT YOUR CODE HERE
    # Access the training data using "data_train[i][j]"
    # Training data contains 3 cols per row: X in
    # index 0, Y in index 1 and Class in index 2
    # Access the test data using "data_test[i][j]"
    # Test data contains 2 cols per row: X in
    # index 0 and Y in index 1, and a blank space in index 2
    # to be filled with class
    # The class value could be a 0 or a 8
    rate = .01
    weights = [[0, 0, 0] for x in range(9)]
    loops = 0

    while loops < 2800:
        loops += 1

        for data in data_train:
            feature = [data[0], data[1], 1]
            prediction = arg_max(weights, feature)  # arg_max should range 1-8
            if prediction != data[2]:
                weights[int(data[2])] = vec_add(weights[int(data[2])], scale(feature, rate))
                weights[prediction] = vec_sub(weights[prediction], scale(feature, rate))

    for data in data_test:
        result = []
        for weight in weights:
            result.append(sum(x_i * y_i for x_i, y_i in zip(weight, [data[0], data[1], 1])))

        data[2] = result.index(max(result))

    return
