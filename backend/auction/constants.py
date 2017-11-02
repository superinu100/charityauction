AUCTION_STATUS_PREVIEW = 'preview'
AUCTION_STATUS_OPEN = 'open'
AUCTION_STATUS_CANCELLED = 'cancelled'
AUCTION_STATUS_CANCELLED_DUE_TO_NO_BIDS = 'cancelled-no-bids'
AUCTION_STATUS_WAITING_FOR_PAYMENT = 'waiting-for-payment'
AUCTION_STATUS_WAITING_TO_SHIP = 'waiting-to-ship'
AUCTION_STATUS_SHIPPED = 'shipped'
AUCTION_STATUS_FINISHED = 'finished'

AUCTION_STATUS_CHOICES = (
    (AUCTION_STATUS_PREVIEW, 'Preview'),
    (AUCTION_STATUS_OPEN, 'Open'),
    (AUCTION_STATUS_CANCELLED, 'Cancelled'),
    (AUCTION_STATUS_CANCELLED_DUE_TO_NO_BIDS, 'Cancelled due to no bids'),
    (AUCTION_STATUS_WAITING_FOR_PAYMENT, 'Waiting for payment'),
    (AUCTION_STATUS_WAITING_TO_SHIP, 'Waiting to ship'),
    (AUCTION_STATUS_SHIPPED, 'Shipped'),
    (AUCTION_STATUS_FINISHED, 'Finished'),
)


BID_STATUS_ACTIVE = 'active'
BID_STATUS_WON = 'won'
BID_STATUS_LOST = 'lost'
BID_STATUS_REJECTED = 'rejected'

BID_STATUS_CHOICES = (
    (BID_STATUS_ACTIVE, 'Active'),
    (BID_STATUS_WON, 'Won'),
    (BID_STATUS_LOST, 'Lost'),
    (BID_STATUS_REJECTED, 'Rejected'),
)


SHIPMENT_STATUS_SHIPPING = 'shipping'
SHIPMENT_STATUS_RETURNING = 'returning'
SHIPMENT_STATUS_ARRIVED = 'arrived'
SHIPMENT_STATUS_CANCELLED = 'cancelled'

SHIPMENT_STATUS_CHOICES = (
    (SHIPMENT_STATUS_SHIPPING, 'Shipping'),
    (SHIPMENT_STATUS_RETURNING, 'Returning'),
    (SHIPMENT_STATUS_ARRIVED, 'Arrived'),
    (SHIPMENT_STATUS_CANCELLED, 'Cancelled'),
)
