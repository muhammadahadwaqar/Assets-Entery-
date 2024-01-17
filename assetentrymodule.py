from asset import Asset

class AssetEntryModule:
    def __init__(self):
        self.assets = []

    def add_asset(self, name, category, value):
        asset = Asset(name, category, value)
        self.assets.append(asset)
        print(f"Asset '{asset.name}' added successfully.")

    def display_assets(self):
        if not self.assets:
            print("No assets found.")
        else:
            print("Assets:")
            for asset in self.assets:
                print(f"Name: {asset.name}, Category: {asset.category}, Value: {asset.value}")