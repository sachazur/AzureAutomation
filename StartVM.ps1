Param($vmname,
      $RGname
     )
$Conn = Get-AutomationConnection -Name AzureRunAsConnection
Add-AzureRMAccount -ServicePrincipal -Tenant $Conn.TenantID -ApplicationId $Conn.ApplicationID -CertificateThumbprint $Conn.CertificateThumbprint
     
get-azurermvm  -name $vmname -resourcegroupname $RGname | Start-Azurermvm -name  $vmname 
Write-host "Hello World"