def main() -> None:
    point_2d: tuple[float, float] = (1.5, 2.25)
    tuple_size: int = len(point_2d)

    print(f"Tuple size: {tuple_size}")

    print(point_2d[0])
    print(point_2d[1], end="\n\n")

    other_point_2d: tuple[float, float] = point_2d
    (coord_x, coord_y) = other_point_2d

    print(coord_x)
    print(coord_y)


if __name__ == "__main__":
    main()
