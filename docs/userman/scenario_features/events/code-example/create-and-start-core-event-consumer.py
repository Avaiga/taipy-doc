from time import sleep

from taipy.core.notification import CoreEventConsumerBase, Event, Notifier


# Define a custom event consumer.
class MyEventConsumer(CoreEventConsumerBase):
    def process_event(self, event: Event):
        # Custom event processing logic here
        print(f"Received a {event.entity_type} {event.operation} event at : {event.creation_date}")


if __name__ == "__main__":
    import taipy as tp
    from taipy import Config

    # Create a scenario configuration.
    some_datanode_cfg = Config.configure_data_node("data", default_data="Some content.")
    print_task_cfg = Config.configure_task("print", print, some_datanode_cfg)
    scenario_config = Config.configure_scenario("scenario", [print_task_cfg])

    # Run the core service.
    orchestrator = tp.Orchestrator().run()

    # Register to the Notifier to retrieve a registration id and a registered queue.
    registration_id, registered_queue = Notifier.register()

    # Create a consumer and start it.
    consumer = MyEventConsumer(registration_id, registered_queue)
    consumer.start()

    # The scenario creation and submission will trigger event emissions.
    scenario = tp.create_scenario(scenario_config)
    submission = tp.submit(scenario)

    # The events are processed in parallel by the consumer.
    # So we need to wait for the consumer to process the events.
    sleep(1)

    # Stop the consumer and unregister from the Notifier.
    consumer.stop()
    Notifier.unregister(registration_id)
