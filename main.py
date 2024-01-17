from asset import Asset
from assetentrymodule import AssetEntryModule

asset_module = AssetEntryModule()

asset_module.add_asset("Laptop", "Electronics", 1200)
asset_module.add_asset("Desk", "Furniture", 500)

asset_module.display_assets()