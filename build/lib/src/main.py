import click
from pathlib import Path
from src.process import process_file


@click.command()
@click.option("--input_dir",type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("--input_file", type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option("--output_dir", required=True)
@click.option("--chunk_size", default=1000)
@click.option("--overlap", default=200)
@click.option("--recreate", is_flag=True, help="Recreate the JSONL files in the directory.")
@click.option("--clear_dir", is_flag=True, help="clears output_dir completely")
def main(input_dir,input_file, output_dir, chunk_size,overlap, recreate, clear_dir):
    if not input_dir and not input_file:
        raise click.BadParameter("You must specify either the directory (--input_dir) or the file (--input_file).")

    if clear_dir:
        output_path = Path(output_dir)

        for item in output_path.iterdir():
            if item.is_file():
                print(f"Deleting file: {item}")
                item.unlink()
            elif item.is_dir():
                print(f"Deleting directory: {item}")
                import shutil
                shutil.rmtree(item)

    if input_dir:
        for file in Path(input_dir).glob("*.pdf"):
            process_file(file, output_dir, chunk_size, overlap,recreate)

    if input_file:
        input_path = Path(input_file)
        process_file(input_path , output_dir, chunk_size, overlap,recreate)



if __name__ == "__main__":
    main()