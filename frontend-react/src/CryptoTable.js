import {
  Box,
  Typography,
  CircularProgress,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import "./CryptoTable.css";
import { useCryptoData } from "./hooks/useCryptoData";
import { getColumns } from "./utils/columns";
import { formatCurrency ,formatPercent } from "./utils/formatters";
import { TableResult, TableValorInvestido, TableValorAtual } from "./components/formatterTables";

export default function CryptoTable() {
  const { cryptos, result_total, loading } = useCryptoData();
  const columns = getColumns();

  return (
    <Box className="custom-box1">
      <Paper className="custom-paper1">
        <Typography className="custom-typography1">
          Carteira do Milhão
        </Typography>
        <Typography variant="subtitle1" align="center" color="white">
          Acompanhe sua carteira de criptomoedas em tempo real
        </Typography>
      </Paper>

      <Paper className="custom-paper2">
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell className="custom-table">
                  Valor total investido
                </TableCell>
                <TableCell className="custom-table">
                  Valor total atual
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow>
                <TableCell className="custom-table">
                  <TableValorInvestido 
                    valueTotalInvestido={ result_total[0]?.valor_total_investido }
                  />
                </TableCell>
                <TableCell className="custom-table">
                  <TableValorAtual
                    valueTotalAtual={ result_total[0]?.valor_total_atual }
                    valueInvestido={result_total[0]?.valor_total_investido}
                    valueAtual={result_total[0]?.valor_total_atual}
                  />
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>

      <Paper className="custom-paper2">
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell className="custom-table">
                  Média de Lucros
                </TableCell>
                <TableCell className="custom-table">
                  Média de Perdas
                </TableCell>
                <TableCell className="custom-table">
                  Percentual de Lucros
                </TableCell>
                <TableCell className="custom-table">
                  Percentual de Perdas
                </TableCell>
                <TableCell className="custom-table">
                  Resultado percentual
                </TableCell>
                <TableCell className="custom-table">
                  Resultado total
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow>
                <TableCell className="custom-table">
                  <TableResult 
                      formattedValue={formatCurrency("USD", result_total[0]?.resultado_ganho)} 
                      value={result_total[0]?.resultado_ganho} 
                    />
                </TableCell>
                <TableCell className="custom-table">
                  <TableResult 
                      formattedValue={formatCurrency("USD", result_total[0]?.resultado_perda)} 
                      value={result_total[0]?.resultado_perda} 
                    />
                </TableCell>
                <TableCell className="custom-table">
                  <TableResult
                      formattedValue={formatPercent(result_total[0]?.resultado_ganho_perc)}
                      value={result_total[0]?.resultado_ganho_perc}
                    />
                </TableCell>
                <TableCell className="custom-table">
                  <TableResult
                      formattedValue={formatPercent(result_total[0]?.resultado_perda_perc)}
                      value={result_total[0]?.resultado_perda_perc}
                    />
                </TableCell>
                <TableCell className="custom-table">
                  <TableResult
                      formattedValue={formatPercent(result_total[0]?.resultado_total_perc)}
                      value={result_total[0]?.resultado_total_perc}
                    />
                </TableCell>
                <TableCell className="custom-table">
                  <TableResult
                      formattedValue={formatCurrency("USD", result_total[0]?.resultado_total_lucro)}
                      value={result_total[0]?.resultado_total_lucro}
                    />
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>

      <Paper className="custom-paper2">
        {loading ? (
          <Box className="custom-box">
            <CircularProgress size={60} />
          </Box>
        ) : (
          <DataGrid
            rows={cryptos}
            columns={columns}
            autoHeight={false}
            style={{ height: 600 }}
            pageSize={15}
            rowsPerPageOptions={[15, 30, 50]}
            className="custom-data-grid"
            disableSelectionOnClick
          />
        )}
      </Paper>
    </Box>
  );
}