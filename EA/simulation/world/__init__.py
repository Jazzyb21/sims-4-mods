try:
    import _lot
except ImportError:

    class _lot:

        @staticmethod
        def get_lot_id_from_instance_id(*_, **__):
            return 0

        class Lot:
            pass
get_lot_id_from_instance_id = _lot.get_lot_id_from_instance_id