adapter_type = {'Ethernet':[], 'Others':[], 'Wireless+External':[],  'unknownVPN':[], 'External':[], 'Onboard':[],  'Wireless':[], 'VPN':[], 'VirtualAdapter':[], 'Ethernet+External':[], 'Ethernet+Onboard':[], 'Wireless+Onboard':[]}
judge_type = {'Ethernet':[], 'Others':[], 'Wireless+External':[],  'unknownVPN':[], 'External':[], 'Onboard':[],  'Wireless':[], 'VPN':[], 'VirtualAdapter':[], 'Ethernet+External':[], 'Ethernet+Onboard':[], 'Wireless+Onboard':[]}

d = {"Intel(R) Ethernet Connection I217-LM Network Adapter":"Ethernet+Onboard",
"Intel(R) Centrino(R) Wireless-N 1000 Network Adapter":"Wireless+Onboard",
"Fast Ethernet CardBus PC Card":"Ethernet",
"数据包计划程序微型端口":"Others",
"Microsoft Tun Miniport Adapter":"Others",
"Microsoft KM-TEST Loopback Adapter":"Others",
"Intel(R) WiFi Link 1000 BGN Network Adapter":"Wireless+Onboard",
"Realtek PCIe GBE 系列控制器":"Ethernet+Onboard",
"Cisco Systems VPN Adapter for 64-bit Windows Network Adapter":"unknownVPN",
"Qualcomm Atheros AR8171/8175 PCI-E Gigabit Ethernet Controller (NDIS 6.20)":"Ethernet+Onboard",
"Intel(R) Centrino(R) Wireless-N 1030":"Wireless+Onboard",
"Broadcom NetLink (TM) Gigabit Ethernet Network Adapter":"Ethernet",
"Realtek RTL8192EU Wireless LAN 802.11n USB 2.0 Network Adapter":"Wireless+External",
"Broadcom 802.11g Network Adapter Network Adapter":"Wireless",
"Intel(R) Centrino(R) Wireless-N 135 Network Adapter":"Wireless+Onboard",
"Realtek 8811CU Wireless LAN 802.11ac USB NIC":"Wireless+External",
"Generic Marvell Yukon 88E8001/8003/8010 based Ethernet Controller Network Adapter":"Ethernet",
"DW1501 Wireless-N WLAN Half-Mini 卡 Network Adapter":"Wireless",
"Realtek RTL8102E/RTL8103E Family PCI-E Fast Ethernet NIC":"Ethernet+Onboard",
"Atheros AR8131 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"ASIX AX88179 USB 3.0 to Gigabit Ethernet Adapter":"Ethernet+External",
"QF9700 USB2.0 To Fast Ethernet Adapter Network Adapter":"Ethernet+External",
"Qualcomm Atheros AR8171/8175 PCI-E Gigabit Ethernet Controller (NDIS 6.30) Network Adapter":"Ethernet+Onboard",
"NVIDIA nForce Networking Controller Network Adapter":"Onboard",
"Intel(R) 82577LM Gigabit Network Connection":"Ethernet+Onboard",
"Atheros AR9485WB-EG Wireless Network Adapter":"Wireless",
"Broadcom 440x 10/100 Integrated Controller":"Others",
"Realtek 8821AE Wireless LAN 802.11ac PCI-E NIC Network Adapter":"Wireless+Onboard",
"Intel(R) 82562V-2 10/100 Network Connection":"Onboard",
"Realtek RTL8168C(P)/8111C(P) 系列 PCI-E 千兆以太网 NIC (NDIS 6.20)":"Onboard",
"FAST Wireless N Adapter Network Adapter":"Wireless",
"802.11n USB Wireless LAN Card":"Wireless+External",
"Broadcom 802.11ac Network Adapter Network Adapter":"Wireless",
"Microsoft Wi-Fi Direct Virtual Adapter":"VirtualAdapter",
"1394 网络适配器":"Others",
"Atheros AR8121/AR8113/AR8114 PCI-E Ethernet Controller Network Adapter":"Ethernet+Onboard",
"MERCURY Wireless N Adapter":"Wireless",
"Realtek RTL8192FU Wireless LAN 802.11n USB 2.0 Network Adapter":"Wireless+External",
"VMware Virtual Ethernet Adapter for VMnet9":"VirtualAdapter",
"Intel(R) Ethernet Connection (5) I219-LM Network Adapter":"Ethernet+Onboard",
"Realtek PCIe GbE Family Controller Network Adapter":"Ethernet+Onboard",
"Atheros AR8121/AR8113/AR8114 PCI-E Ethernet Controller":"Ethernet+Onboard",
"Intel(R) Centrino(R) Wireless-N 2230":"Wireless+Onboard",
"HP EN1207D-TX PCI 10/100 Fast Ethernet Adapter":"Ethernet+Onboard",
"JMicron PCI Express Gigabit Ethernet Adapter":"Ethernet+Onboard",
"Realtek USB FE Family Controller":"External",
"ASIX AX88772B USB2.0 to Fast Ethernet Adapter":"Ethernet+External",
"Realtek RTL8188CE Wireless LAN 802.11n PCI-E NIC":"Wireless+Onboard",
"Intel(R) Wireless-AC 9560 160MHz":"Wireless+Onboard",
"Intel(R) 82578DC Gigabit Network Connection":"Ethernet+Onboard",
"Realtek RTL8168D(P)/8111D(P) PCI-E Gigabit Ethernet NIC":"Ethernet+Onboard",
"Realtek RTL8101E 系列 PCI-E 快速以太网 NIC (NDIS 6.20)":"Onboard",
"Atheros AR9485 Wireless Network Adapter Network Adapter":"Wireless",
"Intel(R) Ethernet Connection (2) I219-LM Network Adapter":"Ethernet+Onboard",
"RAS Async Adapter":"Others",
"Intel(R) Dual Band Wireless-AC 8275 Network Adapter":"Wireless+Onboard",
"VIA Velocity-Family Gigabit Ethernet Adapter Network Adapter":"Ethernet",
"Qualcomm Atheros AR8171/8175 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"1x1 11bgn Wireless LAN PCI Express Half Mini Card Adapter Network Adapter":"Wireless+Onboard",
"Tlink TL9200 USB2.0 To Fast Ethernet Adapter":"Ethernet+External",
"VIA Velocity-Family Gigabit Ethernet Adapter":"Ethernet",
"Atheros AR8132 PCI-E Fast Ethernet Controller":"Ethernet+Onboard",
"2x2 11b/g/n Wireless LAN Network Adapter":"Wireless",
"Dell Wireless 1502 802.11b/g/n Network Adapter":"Wireless",
"Qualcomm Atheros AR9285 Wireless Network Adapter":"Wireless",
"Intel(R) Dual Band Wireless-AC 8260":"Wireless+Onboard",
"Realtek RTL8139 Family PCI Fast Ethernet NIC":"Ethernet+Onboard",
"Cisco Systems VPN Adapter for 64-bit Windows":"unknownVPN",
"1x1 11b/g/n Wireless LAN PCI Express Half Mini Card Adapter Network Adapter":"Wireless+Onboard",
"Intel(R) I210 Gigabit Network Connection Network Adapter":"Ethernet+Onboard",
"Realtek RTL8188EE Wireless LAN 802.11n PCI-E NIC Network Adapter":"Wireless+Onboard",
"Qualcomm Atheros AR5BWB222 Wireless Network Adapter Network Adapter":"Wireless",
"Teefer2 Miniport":"Others",
"1x1 11b/g/n Wireless LAN PCI Express Half Mini Card Adapter":"Wireless+Onboard",
"Intel(R) PRO/100 VE Network Connection":"Onboard",
"Marvell Yukon 88E8039 PCI-E Fast Ethernet Controller Network Adapter":"Ethernet+Onboard",
"Intel(R) 82567LM-3 Gigabit Network Connection Network Adapter":"Ethernet+Onboard",
"Intel(R) 82566DM-2 Gigabit Network Connection":"Ethernet+Onboard",
"Cifernet Virtual Adapter":"VirtualAdapter",
"Dell Wireless 1707 802.11b/g/n (2.4GHZ) Network Adapter":"Wireless",
"Intel(R) Ethernet Connection I217-LM":"Ethernet+Onboard",
"AMD PCNET Family PCI Ethernet Adapter":"Ethernet+Onboard",
"Realtek Common Ethernet Controllers":"Ethernet",
"Intel(R) Dual Band Wireless-N 7260 Network Adapter":"Wireless+Onboard",
"Intel(R) 82578DM Gigabit Network Connection":"Ethernet+Onboard",
"Realtek PCI GbE Family Controller Network Adapter":"Ethernet+Onboard",
"Marvell Yukon 88E8040 PCI-E Fast Ethernet Controller Network Adapter":"Ethernet+Onboard",
"Intel(R) Dual Band Wireless-AC 3165 Network Adapter":"Wireless+Onboard",
"Adt IpSec Miniport":"Others",
"DM9601 USB To Fast Ethernet Adapter(KMDF)":"Ethernet+External",
"Ralink RT3090 802.11n WiFi Adapter Network Adapter":"Wireless",
"ADMtek AN983 based ethernet adapter":"Ethernet",
"Intel(R) PRO/100 S Desktop Adapter":"Onboard",
"Sangfor FastIO Ethernet Adapter":"Ethernet",
"Qualcomm Atheros AR956x Wireless Network Adapter Network Adapter":"Wireless",
"Intel(R) 82579LM Gigabit Network Connection":"Ethernet+Onboard",
"Realtek RTL8139C  Fast Ethernet NIC":"Ethernet",
"CH9200 USB Ethernet Adapter Network Adapter":"Ethernet+External",
"Intel(R) 82577LM Gigabit Network Connection Network Adapter":"Ethernet+Onboard",
"Killer E2200 Gigabit Ethernet Controller":"Ethernet",
"Wireless N Adapter":"Wireless",
"基于 Marvell Yukon 88E8057 PCI-E 的通用千兆以太网控制器":"Onboard",
"Realtek PCIe GbE Family Controller":"Ethernet+Onboard",
"Intel(R) Wireless-AC 9260 160MHz":"Wireless+Onboard",
"Atheros AR9485 Wireless Network Adapter":"Wireless",
"ASIX AX88772A USB2.0 to Fast Ethernet Adapter":"Ethernet+External",
"3Com EtherLink XL 10/100 PCI TX NIC (3C905B-TX)":"Onboard",
"Intel(R) Wireless-AC 9560 Network Adapter":"Wireless+Onboard",
"Broadcom 4313GN 802.11b/g/n 1x1 Wi-Fi 适配器 Network Adapter":"Wireless",
"Realtek USB FE Family Controller Network Adapter":"External",
"Marvell Yukon 88E8055 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"ADT Filter Miniport":"Others",
"VMware Accelerated AMD PCNet Adapter":"Onboard",
"Atheros AR8152/8158 PCI-E Fast Ethernet Controller":"Ethernet+Onboard",
"Realtek RTL8168B/8111B 系列 PCI-E 千兆以太网 NIC (NDIS 6.20)":"Onboard",
"Qualcomm Atheros AR9485 Wireless Network Adapter Network Adapter":"Wireless",
"Realtek RTL8188EU Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"Realtek PCI GBE 系列控制器 Network Adapter":"Ethernet+Onboard",
"NVIDIA nForce 10/100 Mbps Ethernet  Network Adapter":"Ethernet+Onboard",
"Tencent Network Miniport":"Others",
"54M Wireless USB Adapter":"Wireless+External",
"Broadcom 802.11ac Network Adapter":"Wireless",
"Realtek RTL8192EU Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"Realtek 8821AE Wireless LAN 802.11ac PCI-E NIC":"Wireless+Onboard",
"Realtek RTL8821CE 802.11ac PCIe Adapter Network Adapter":"Wireless+Onboard",
"Apple Mobile Device Ethernet":"Ethernet",
"Microsoft Hyper-V Network Adapter":"VirtualAdapter",
"TP-LINK Wireless USB Adapter Network Adapter":"Wireless+External",
"Qualcomm Atheros AR8162/8166/8168 PCI-E Fast Ethernet Controller (NDIS 6.20)":"Ethernet+Onboard",
"NVIDIA nForce Networking Controller":"Onboard",
"Realtek RTL8168C(P)/8111C(P) PCI-E Gigabit Ethernet NIC":"Ethernet+Onboard",
"Broadcom NetLink (TM) Fast Ethernet":"Ethernet",
"Intel(R) Ethernet Connection (5) I219-V Network Adapter":"Ethernet+Onboard",
"Realtek PCIe FE Family Controller Network Adapter":"Onboard",
"Xiaomi 802.11n USB Wireless Adapter":"Wireless+External",
"1x1 11b/g/n 无线局域网 PCI Express Half Mini Card 适配器":"Onboard",
"Atheros AR9485WB-EG Wireless Network Adapter Network Adapter":"Wireless",
"Marvell Yukon 88E8039 PCI-E Fast Ethernet Controller":"Ethernet+Onboard",
"Dell 无线 1510 Wireless-N WLAN Mini-Card Network Adapter":"Wireless",
"SSLVPN Virtual Network Adapter(CS Support)":"unknownVPN",
"Intel(R) Ethernet Connection (4) I219-V":"Ethernet+Onboard",
"Microsoft Virtual WiFi Miniport Adapter Network Adapter":"VirtualAdapter",
"VirtualBox Host-Only Ethernet Adapter":"VirtualAdapter",
"Qualcomm Atheros AR9485WB-EG Wireless Network Adapter Network Adapter":"Wireless",
"Qualcomm QCA9565 802.11b/g/n Wireless Adapter":"Wireless",
"Marvell Yukon 88E8040 PCI-E Fast Ethernet Controller":"Ethernet+Onboard",
"Realtek Common Ethernet Controllers Network Adapter":"Ethernet",
"1x1 11b/g/n 无线局域网 PCI Express Half Mini Card 适配器 Network Adapter":"Onboard",
"Realtek PCI GBE Family Controller Network Adapter":"Ethernet+Onboard",
"Qualcomm Atheros AR8161/8165 PCI-E Gigabit Ethernet Controller (NDIS 6.20) Network Adapter":"Ethernet+Onboard",
"Cisco Systems VPN Adapter Network Adapter":"unknownVPN",
"Qualcomm Atheros AR8151 PCI-E Gigabit Ethernet Controller (NDIS 6.20)":"Ethernet+Onboard",
"IPvE Adapter":"Others",
"Microsoft TV/Video Connection":"Others",
"Belkin 54g Wireless USB Network Adapter":"Wireless+External",
"Atheros AR9285 Wireless Network Adapter":"Wireless",
"Tencent 802.11n USB Wireless Adapter":"Wireless+External",
"Intel(R) 82574L Gigabit Network Connection":"Ethernet+Onboard",
"Marvell Yukon 88E8070 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"WAN 微型端口 (IP)":"Others",
"Intel(R) Ethernet Connection (2) I218-V Network Adapter":"Ethernet+Onboard",
"Intel(R) 82567LF Gigabit Network Connection":"Ethernet+Onboard",
"Realtek PCIe GBE Family Controller":"Ethernet+Onboard",
"Broadcom 802.11ac 网络适配器 Network Adapter":"Wireless",
"MERCURY Wireless N Adapter Network Adapter":"Wireless",
"Broadcom NetXtreme Gigabit Ethernet Network Adapter":"Ethernet",
"TP-LINK Wireless USB Adapter":"Wireless+External",
"Qualcomm Atheros AR8151 PCI-E Gigabit Ethernet Controller (NDIS 6.20) Network Adapter":"Ethernet+Onboard",
"Intel(R) Dual Band Wireless-AC 3160":"Wireless+Onboard",
"Qualcomm QCA9565 802.11b/g/n Wireless Adapter Network Adapter":"Wireless",
"SecTap Adapter":"Others",
"DM9621A USB To Fast Ethernet Adapter(KMDF)":"Ethernet+External",
"Realtek PCIe GBE Family Controller Network Adapter":"Ethernet+Onboard",
"Broadcom 802.11n 网络适配器 Network Adapter":"Wireless",
"Sangfor SSL VPN CS Support System VNIC":"VPN",
"Realtek RTL8723BE Wireless LAN 802.11n PCI-E NIC":"Wireless+Onboard",
"Marvell Yukon 88E8057 Family PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"Intel(R) Ethernet Connection I217-V":"Ethernet+Onboard",
"Intel(R) PRO/100 VE Network Connection Network Adapter":"Onboard",
"NVIDIA nForce 10/100 Mbps Ethernet ":"Ethernet+Onboard",
"Qualcomm Atheros AR8161/8165 PCI-E Gigabit Ethernet Controller (NDIS 6.20)":"Ethernet+Onboard",
"Atheros AR2427 Wireless Network Adapter Network Adapter":"Wireless",
"Intel(R) Ethernet Connection (5) I219-LM":"Ethernet+Onboard",
"Qualcomm Atheros AR9285 Wireless Network Adapter Network Adapter":"Wireless",
"Broadcom 802.11n 网络适配器":"Wireless",
"Dell Wireless 1506 802.11b/g/n (2.4GHz)":"Wireless",
"Realtek RTL8168D/8111D 系列 PCI-E 千兆以太网 NIC (NDIS 6.20) Network Adapter":"Onboard",
"Realtek RTL8723DE 802.11b/g/n PCIe Adapter":"Wireless+Onboard",
"USB to Ethernet Adapter":"Ethernet+External",
"Realtek RTL8102E/RTL8103E 系列 PCI-E 快速以太网 NIC (NDIS 6.20)":"Onboard",
"VIA Rhine III Compatible Fast Ethernet Adapter":"Ethernet",
"NVIDIA nForce 10/100/1000 Mbps Ethernet ":"Ethernet+Onboard",
"Atheros AR9485 802.11b/g/n WiFi Adapter":"Wireless",
"3Com 3C905TX-based Ethernet Adapter (Generic)":"Ethernet",
"Realtek PCIe FE Family Controller":"Onboard",
"Dell Wireless 1810 802.11ac Network Adapter":"Wireless",
"Intel(R) Ethernet Connection I217-V Network Adapter":"Ethernet+Onboard",
"Deterministic Network Enhancer Miniport":"Others",
"ASUS 802.11g 网络适配器 Network Adapter":"Wireless",
"Marvell Yukon 88E8056 PCI-E Gigabit Ethernet Controller Network Adapter":"Ethernet+Onboard",
"Generic Marvell Yukon 88E8057 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"FAST Wireless N Adapter":"Wireless",
"Intel(R) PRO/1000 MT Network Connection":"Onboard",
"TAP-Windows Adapter V9":"Others",
"VMware Virtual Ethernet Adapter for VMnet8":"VirtualAdapter",
"HP NetServer 10/100TX PCI LAN Adapter":"Onboard",
"Realtek RTL8139/810x Family Fast Ethernet NIC":"Ethernet",
"Realtek RTL8191SU Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"VIA Velocity Family Gigabit Ethernet Adapter":"Ethernet",
"Rising RfwNdis Driver":"Others",
"Intel(R) Wireless-N 7265":"Wireless+Onboard",
"Broadcom NetXtreme Gigabit Ethernet":"Ethernet",
"11b/g/n  Wireless LAN Mini-PCI Express Adapter II Network Adapter":"Wireless+Onboard",
"Intel(R) Centrino(R) Advanced-N 6205 Driver Network Adapter":"Onboard",
"Realtek USB GbE Family Controller":"Ethernet+External",
"Qualcomm Atheros QCA9377 Wireless Network Adapter Network Adapter":"Wireless",
"DAVICOM 9102/A PCI Fast Ethernet Adapter ":"Ethernet+Onboard",
"Broadcom 802.11g 网络适配器 Network Adapter":"Wireless",
"Realtek RTL8188EU Wireless LAN 802.11n USB 2.0 Network Adapter":"Wireless+External",
"VMware Virtual Ethernet Adapter for VMnet1":"VirtualAdapter",
"Realtek RTL8139/810x Family Fast Ethernet NIC Network Adapter":"Ethernet",
"Intel(R) Dual Band Wireless-AC 3165":"Wireless+Onboard",
"RD9700 USB2.0 To Fast Ethernet Adapter":"Ethernet+External",
"Realtek PCI GBE Family Controller":"Ethernet+Onboard",
"Remote NDIS based Internet Sharing Device Network Adapter":"Others",
"Realtek 8188GU Wireless LAN 802.11n USB NIC":"Wireless+External",
"Intel(R) Centrino(R) Advanced-N 6200 AGN Network Adapter":"Onboard",
"Intel(R) 82578DM Gigabit Network Connection Network Adapter":"Ethernet+Onboard",
"Infineon AN983B PCI Based Fast Ethernet Adapter":"Ethernet+Onboard",
"Intel(R) Ethernet Connection (2) I219-V Network Adapter":"Ethernet+Onboard",
"WinpkFilter Miniport":"Others",
"Fortinet virtual adapter":"VirtualAdapter",
"Intel(R) Wireless-N 7260":"Wireless+Onboard",
"Atheros AR8132 PCI-E Fast Ethernet Controller (NDIS 6.20)":"Ethernet+Onboard",
"Qualcomm Atheros AR946x Wireless Network Adapter Network Adapter":"Wireless",
"Cisco Systems VPN Adapter":"unknownVPN",
"QF9700 USB2.0 To Fast Ethernet Adapter":"Ethernet+External",
"Intel(R) Centrino(R) Wireless-N 2230 Network Adapter":"Wireless+Onboard",
"Intel(R) Ethernet Connection I218-V":"Ethernet+Onboard",
"Realtek RTL8188ETV Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"Intel(R) Ethernet Connection (2) I219-V":"Ethernet+Onboard",
"Intel(R) Dual Band Wireless-AC 7265":"Wireless+Onboard",
"Realtek Gaming GBE Family Controller Network Adapter":"Ethernet",
"Marvell Yukon 88E8056 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"VirtualBox Bridged Networking Driver Miniport":"VirtualAdapter",
"Wireless Lite N Adapter":"Wireless",
"11b/g/n  Wireless LAN Mini-PCI Express Adapter II":"Wireless+Onboard",
"Atheros AR5B125 Wireless Network Adapter Network Adapter":"Wireless",
"Intel(R) PRO/100 Network Connection":"Onboard",
"WAN 微型端口 (PPPOE)":"Others",
"Atheros AR8161/8165 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"ADMtek AN983 10/100Mbps PCI Adapter":"Onboard",
"Marvell Yukon 88E8057 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"Network Filter Driver Miniport":"Others",
"Intel(R) Centrino(R) Wireless-N 1030 Network Adapter":"Wireless+Onboard",
"Intel(R) Ethernet Connection (7) I219-LM":"Ethernet+Onboard",
"Intel(R) Dual Band Wireless-AC 3160 Network Adapter":"Wireless+Onboard",
"Intel(R) Centrino(R) Wireless-N 1000":"Wireless+Onboard",
"Realtek RTL8723B Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"Realtek 8188GU Wireless LAN 802.11n USB NIC Network Adapter":"Wireless+External",
"Intel(R) Wireless-N 7260 Network Adapter":"Wireless+Onboard",
"TP-Link Gigabit PCI Express Adapter":"Ethernet+Onboard",
"Dell 无线 1701 802.11b/g/n Network Adapter":"Wireless",
"Realtek Gaming GbE Family Controller Network Adapter":"Ethernet",
"WAN 微型端口 (PPTP)":"Others",
"Microsoft Virtual WiFi Miniport Adapter":"VirtualAdapter",
"Realtek 8821CE Wireless LAN 802.11ac PCI-E NIC":"Wireless+Onboard",
"Intel(R) Ethernet Connection (7) I219-LM Network Adapter":"Ethernet+Onboard",
"CH9200 USB Ethernet Adapter":"Ethernet+External",
"Atheros AR5B97 Wireless Network Adapter Network Adapter":"Wireless",
"360 Wifi QHNAT Miniport":"Wireless",
"Dell Wireless 1703 802.11b/g/n (2.4GHz) Network Adapter":"Wireless",
"Hyper-V Virtual Ethernet Adapter":"VirtualAdapter",
"Killer e2200 Gigabit Ethernet Controller":"Ethernet",
"Dell 无线 1704 802.11b/g/n (2.4GHz)":"Wireless",
"Broadcom NetXtreme Gigabit Ethernet Plus":"Ethernet",
"Intel(R) Ethernet Connection (3) I218-LM":"Ethernet+Onboard",
"Intel(R) Centrino(R) Advanced-N 6205 Network Adapter":"Onboard",
"Qualcomm Atheros AR8171/8175 PCI-E Gigabit Ethernet Controller (NDIS 6.20) Network Adapter":"Ethernet+Onboard",
"Fortinet SSL VPN Virtual Ethernet Adapter":"unknownVPN",
"Qualcomm Atheros AR8161 PCI-E Gigabit Ethernet Controller (NDIS 6.30)":"Ethernet+Onboard",
"Intel(R) Centrino(R) Advanced-N 6205":"Onboard",
"Dell Wireless 1707 802.11b/g/n (2.4GHZ)":"Wireless",
"Intel(R) Ethernet Connection (3) I218-V":"Ethernet+Onboard",
"Intel(R) Ethernet Connection (5) I219-V":"Ethernet+Onboard",
"RAS 同步适配器":"Others",
"Intel(R) 82567LF-3 Gigabit Network Connection":"Ethernet+Onboard",
"Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"1x1 11bgn Wireless LAN PCI Express Half Mini Card Adapter":"Wireless+Onboard",
"Realtek RTL8168/8111 PCI-E Gigabit Ethernet NIC":"Ethernet+Onboard",
"Qualcomm Atheros QCA9377 Wireless Network Adapter":"Wireless",
"Qualcomm Atheros AR8152/8158 PCI-E Fast Ethernet Controller (NDIS 6.20) Network Adapter":"Ethernet+Onboard",
"Realtek RTL8188CU Wireless LAN 802.11n USB 2.0 Network Adapter":"Wireless+External",
"Intel(R) Ethernet Connection I218-LM":"Ethernet+Onboard",
"Bluetooth 设备(个人区域网)":"Others",
"iNode VPN Virtual NIC":"unknownVPN",
"Intel(R) 82566DM-2 Gigabit Network Connection Network Adapter":"Ethernet+Onboard",
"Remote NDIS based Device":"Others",
"Intel(R) Dual Band Wireless-AC 8265":"Wireless+Onboard",
"Qualcomm Atheros AR8161 PCI-E Gigabit Ethernet Controller (NDIS 6.30) Network Adapter":"Ethernet+Onboard",
"Intel(R) WiFi Link 5100 AGN Network Adapter":"Wireless+Onboard",
"Intel(R) Ethernet Connection I219-V":"Ethernet+Onboard",
"Marvell AVASTAR Wireless-AC Network Controller":"Wireless",
"Intel(R) Dual Band Wireless-AC 8265 Network Adapter":"Wireless+Onboard",
"Sangfor SSL VPN CS Support System VNIC Network Adapter":"VPN",
"Realtek 8821CE Wireless LAN 802.11ac PCI-E NIC Network Adapter":"Wireless+Onboard",
"Atheros AR8161/8165 PCI-E Gigabit Ethernet Controller (NDIS 6.20)":"Ethernet+Onboard",
"Intel(R) Ethernet Connection (2) I219-LM":"Ethernet+Onboard",
"Intel(R) Ethernet I210-T1 GbE NIC":"Ethernet+Onboard",
"Realtek RTL8169/8110 Family Gigabit Ethernet NIC":"Ethernet",
"Intel(R) Centrino(R) Wireless-N 2200 Network Adapter":"Wireless+Onboard",
"ASIX AX88772C USB2.0 to Fast Ethernet Adapter Network Adapter":"Ethernet+External",
"TSNetNdis5 Miniport":"Others",
"RD9700 USB2.0 To Fast Ethernet Adapter Network Adapter":"Ethernet+External",
"2x2 11bgn Wireless LAN":"Wireless",
"Qualcomm Atheros AR956x Wireless Network Adapter":"Wireless",
"LAN7500 USB 2.0 to Ethernet 10/100/1000 Adapter":"Ethernet+External",
"iNode VPN Virtual NIC Network Adapter":"unknownVPN",
"Intel(R) 82567LM-3 Gigabit Network Connection":"Ethernet+Onboard",
"VirtualBox Host-Only Ethernet Adapter Network Adapter":"VirtualAdapter",
"TP-Link Gigabit PCI Express Adapter Network Adapter":"Ethernet+Onboard",
"Intel(R) 82579LM Gigabit Network Connection Network Adapter":"Ethernet+Onboard",
"Realtek PCIe GBE 系列控制器 Network Adapter":"Ethernet+Onboard",
"NVIDIA nForce 10/100/1000 Mbps Ethernet  Network Adapter":"Ethernet+Onboard",
"802.11ac Wireless LAN Card":"Wireless",
"Realtek RTL8191SU Wireless LAN 802.11n USB 2.0 Network Adapter":"Wireless+External",
"802.11n USB Wireless LAN Card Network Adapter":"Wireless+External",
"Intel(R) Ethernet Connection (7) I219-V Network Adapter":"Ethernet+Onboard",
"Intel(R) WiFi Link 5300 AGN":"Wireless+Onboard",
"TeamViewer VPN Adapter":"unknownVPN",
"Atheros AR9285 Wireless Network Adapter Network Adapter":"Wireless",
"OrayVPN Virtual Ethernet Adapter V1":"unknownVPN",
"ASIX AX88772C USB2.0 to Fast Ethernet Adapter":"Ethernet+External",
"Atheros AR8151 PCI-E Gigabit Ethernet Controller":"Ethernet+Onboard",
"Dell Wireless 1703 802.11b/g/n (2.4GHz)":"Wireless",
"Intel(R) Dual Band Wireless-AC 3168 Network Adapter":"Wireless+Onboard",
"Marvell Yukon 88E8057 PCI-E Gigabit Ethernet Controller Network Adapter":"Ethernet+Onboard",
"Broadcom BCM943228HM4L 802.11a/b/g/n 2x2 WiFi 适配器 Network Adapter":"Wireless",
"Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter":"Wireless+External",
"Realtek RTL8188CE Wireless LAN 802.11n PCI-E NIC Network Adapter":"Wireless+Onboard",
"Dell 无线 1704 802.11b/g/n (2.4GHz) Network Adapter":"Wireless",
"Intel(R) Ethernet Connection (7) I219-V":"Ethernet+Onboard",
"USB to Ethernet Adapter Network Adapter":"Ethernet+External",
"Realtek RTL8168D/8111D 系列 PCI-E 千兆以太网 NIC (NDIS 6.20)":"Onboard",
"D-Link DFE-530TX PCI Fast Ethernet Adapter (rev.C)":"Ethernet+Onboard",
"Broadcom NetLink (TM) Gigabit Ethernet":"Ethernet",
"Broadcom NetXtreme 57xx Gigabit Controller":"Ethernet",
"Realtek RTL8188CU Wireless LAN 802.11n USB 2.0 Network Adapter Network Adapter":"Wireless+External",
"Intel(R) Dual Band Wireless-AC 7265 Network Adapter":"Wireless+Onboard",
"Realtek RTL8102E Family PCI-E Fast Ethernet NIC":"Ethernet+Onboard",
"Microsoft Loopback Adapter":"Others",
"Secoway Virtual Adapter":"VirtualAdapter",
"Realtek RTL8723BE Wireless LAN 802.11n PCI-E NIC Network Adapter":"Wireless+Onboard",
"Realtek Gaming GBE Family Controller":"Ethernet"
}

def march_device(s):
    try:
        return(d[s])
    except:
        return("unknown adapter")

# tt = {'Ethernet': ['10.57.116.201'], 'Others': [], 'Wireless+External': ['172.30.235.1'], 'VirtualAdapter': [], 'unknownVPN': [], 'External': [], 'Onboard': [], 'VirtualAdapter': [], 'Wireless': [], 'VPN': [], 'VirtualAdapter': [], 'Ethernet+External': [], 'Ethernet+Onboard': ['133.163.20.101', '10.57.116.201'], 'Wireless+Onboard': []}
# ipl = []
# for key in tt:
#     ips = "+".join(tt[key])
#     if ips:
#         ipl.append(key + ":" + ips)
# adapter_ip = " ".join(ipl)
# print(adapter_ip)