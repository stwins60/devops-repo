resource "aws_customer_gateway" "main" {
  bgp_asn    = 65000
  ip_address = var.customer_gateway_ip
  type       = "ipsec.1"
  
  tags = {
    Name = "${var.name_prefix}-cgw"
  }
}

resource "aws_vpn_gateway" "main" {
  vpc_id = var.vpc_id
  
  tags = {
    Name = "${var.name_prefix}-vgw"
  }
}

resource "aws_vpn_connection" "main" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.main.id
  type                = "ipsec.1"
  static_routes_only  = true
  
  tags = {
    Name = "${var.name_prefix}-vpn"
  }
}

resource "aws_vpn_connection_route" "office" {
  destination_cidr_block = var.on_premise_cidr
  vpn_connection_id      = aws_vpn_connection.main.id
}
