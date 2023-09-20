from utils.logger_config import logger
from utils.context import context
from utils.api_init import naas
from utils.api_init import pgw
from utils.api_init import xpaas


def main():
    logger.info("Physicals - MOCN Extraction Niklas")

    logger.info(naas.api.get_resource_list())
    logger.info(naas.api.clusters.actions)

    naas_cluster = context['NAAS_CLUSTER']

    logger.info("{0} {1} {0}".format("=" * 40, naas_cluster))
    cells = naas.api.clusters.get_cluster_cells(naas_cluster, params={'technology': 'LTE', 'vendor': 'NOKIA',
                                                                      'fields': 'cell._id,cell.name,GREY_SPOT_MOCN'})

    for cell in cells.body['elements']:
        mocn_cell = cell['cell'].get('GREY_SPOT_MOCN')
        #mocn_target = cell['cell']['grey_spot_target']
        if mocn_cell == "TEF4TDG":
            #logger.info(mocn_cell, mocn_target)
            print('mocn_cell:',cell)
        else:
            pass

    """
    workItem = {
                "type": "PHYSICALS",
                "_moId": '602eae36-b93c-3cb4-9d6f-4ddcfab8e830',
                "parameterName": "grey_spot_mocn",
                "value": '3360',
                "maintenanceFlag": "false"
                }
    work_order = {
                    "description": "Physical_Example_Niklas",
                    "method": "NON_TRANSACTION",
                    "mode": "OFFLINE_SIM",
                    "priority": 1,
                    "trackingId": context.get('TRACKING_ID'),
                    "workItems": [workItem]
                }

    work_order_res = pgw.api.workorders.send_workorder(body=work_order)
    logger.info(work_order_res)
    """


if __name__ == '__main__':
    main()

