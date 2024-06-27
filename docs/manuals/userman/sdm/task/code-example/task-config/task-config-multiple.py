from taipy import Config


def multiply_and_add(nb1, nb2):
    return nb1 * nb2, nb1 + nb2


nb_1_cfg = Config.configure_data_node("nb_1", default_data=21)
nb_2_cfg = Config.configure_data_node("nb_2", default_data=2)

multiplication_cfg = Config.configure_data_node("multiplication")
addition_cfg = Config.configure_data_node("addition")

task_cfg = Config.configure_task("foo",
                                 multiply_and_add,
                                 [nb_1_cfg, nb_2_cfg],
                                 [multiplication_cfg, addition_cfg])
