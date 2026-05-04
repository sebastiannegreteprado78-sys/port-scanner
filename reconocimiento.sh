#!/bin/bash
echo "=== REPORTE DE RECONOCIMIENTO ==="
echo "Fecha: $(date)"
echo ""
echo "--- USUARIO ---"
echo "Usuario actual: $(whoami)"
echo ""
echo "--- RED ---"
hostname -I
echo ""
echo "--- PUERTO ABIERTOS ---"
ss -tuln
echo ""
echo "--- PROCESOS ---"
ps aux | head -10
