{ pkgs }: {
  deps = [
    pkgs.python3 run test.py
  ];
}