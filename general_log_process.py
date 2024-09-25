def preprocess_log(input_log_path, start_str, end_str):
    """
    Preprocess the log file, delete the content after the last end_str and before the first start_str in the log.
    :param input_log_path: Source log path
    :param output_log_path: the processed log path
    :param start_str: String identifier at the beginning of each round of log output
    :param end_str: String identifier at the end of each round of log output
    :return: null
    """

    output_log_path = input_log_path.split(".log")[0] + '_preprocessed.log'

    try:
        # 读取日志文件内容
        with open(input_log_path, 'r', encoding='UTF-8', errors='ignore') as file:
            log_lines = file.readlines()

        # 查找第一轮输出位置
        first_separator_index = -1
        for i, line in enumerate(log_lines):
            # print(line)
            if start_str in line:
                first_separator_index = i
                break

        # 查找最后一轮输出结束位置
        last_reset_index = -1
        for i, line in enumerate(reversed(log_lines)):

            if end_str in line:
                last_reset_index = len(log_lines) - i - 1
                break

        if last_reset_index == -1:
            print("ERROR：The log does not record a complete round of output")
            return

        # 删除有效数据之前和之后的内容，即 start_str 和 end_str 之后的内容
        if first_separator_index != -1 and last_reset_index != -1:
            # preprocessed_log_lines = log_lines[first_separator_index - 1:] + log_lines[:last_reset_index + 1]
            preprocessed_log_lines = log_lines[first_separator_index - 1:last_reset_index + 1]

            # 输出预处理后的日志
            with open(output_log_path, 'w') as output_file:
                output_file.writelines(preprocessed_log_lines)

            # print("预处理完成，并将结果保存到 " + output_log_path + " 文件中。")
        else:
            print("No log content matching the criteria was found.")

    except Exception as e:
        print("An error occurred while preprocessing the log: " + str(e))

    return output_log_path
