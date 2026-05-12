param(
    [string]$Source = "",
    [string]$DestinationRoot = "",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($DestinationRoot)) {
    if ($env:CODEX_HOME) {
        $DestinationRoot = Join-Path $env:CODEX_HOME "skills"
    } else {
        $DestinationRoot = Join-Path $HOME ".codex\skills"
    }
}

if ([string]::IsNullOrWhiteSpace($Source)) {
    $Source = Join-Path $PSScriptRoot "ai-level"
}

$Source = (Resolve-Path -LiteralPath $Source).Path
$Destination = Join-Path $DestinationRoot "ai-level"

if (-not (Test-Path -LiteralPath (Join-Path $Source "SKILL.md"))) {
    throw "Source does not look like a Codex skill: $Source"
}

if (Test-Path -LiteralPath $Destination) {
    if (-not $Force) {
        throw "ai-level is already installed at $Destination. Re-run with -Force to overwrite."
    }
    Remove-Item -Recurse -Force -LiteralPath $Destination
}

New-Item -ItemType Directory -Force -Path $DestinationRoot | Out-Null
Copy-Item -Recurse -Force -LiteralPath $Source -Destination $DestinationRoot

Write-Host "Installed ai-level to $Destination"
Write-Host "Restart Codex, then run /ai-level"

