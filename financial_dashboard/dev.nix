{ pkgs, ... }: {
  environment.systemPackages = with pkgs; [
    sudo,
    nixos-rebuild
  ];
}

