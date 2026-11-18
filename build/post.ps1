param([string]$Versao = "07")
$ErrorActionPreference = "Stop"
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
    $d = $w.Documents.Open("D:\tech\tcc\build\${Versao}_raw.docx")
    "equacoes: " + $d.OMaths.Count
    $d.OMaths.BuildUp()
    $d.Fields.Update() | Out-Null
    $d.Repaginate()
    foreach ($t in $d.TablesOfContents) { $t.Update() }
    foreach ($t in $d.TablesOfFigures) { $t.Update() }
    $d.Fields.Update() | Out-Null
    "paginas: " + $d.ComputeStatistics(2)
    $d.SaveAs2("D:\tech\tcc\docs\${Versao}.docx", 16)
    # ExportAsFixedFormat2 com OptimizeForImageQuality = true: não reduz a resolução das figuras no PDF
    try {
        $d.ExportAsFixedFormat2("D:\tech\tcc\docs\${Versao}.pdf", 17, $false, 0, 0, 1, 1, 0, $true, $true, 0, $true, $true, $false, $true)
    } catch {
        "ExportAsFixedFormat2 indisponivel; usando ExportAsFixedFormat"
        $d.ExportAsFixedFormat("D:\tech\tcc\docs\${Versao}.pdf", 17)
    }
    $d.Close($false)
} finally {
    $w.Quit()
}
