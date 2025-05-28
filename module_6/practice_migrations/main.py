#!venv/bin/python
import click

from api.crud import EntityCruder


@click.command()
@click.option(
    "--action",
    required=True,
    type=click.Choice(["create", "delete", "update", "list"]),
)
@click.option("--entity_name", required=True, help="Name of entity.")
@click.option("--entity_id", help="ID of entity to perform action on.")
@click.option("--name", help="Value for entity's main attribute.")
@click.option(
    "--order_by",
    help="Ordering for list of entities.",
    type=click.Choice(["asc", "desc"]),
)
def manager(
    action: str, entity_name: str, entity_id: str, name: str, order_by: bool
) -> None:
    print(f"{action}: {entity_name}: {entity_id}: {name}")
    print(EntityCruder.do_something())

    print(EntityCruder.VALUE)

    cruder = EntityCruder()
    print(cruder.value)

    method_name = f"{action}_{entity_name}"
    to_execute = getattr(cruder, method_name, None)
    if not to_execute:
        raise AttributeError(f"Unknown method_name: {method_name}.")

    to_execute(entity_id=entity_id, name=name, order_by=order_by)


if __name__ == "__main__":
    try:
        manager()
    except (ValueError, AttributeError, TypeError) as err:
        print(f"Error: {err}")
