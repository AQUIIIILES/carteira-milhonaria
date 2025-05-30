import { formatCurrency, formatQuantity, formatCurrencyLucro, formatPercent } from "./formatters";
import {GridHeader, GridTitle, GridRow, GridRowLucro } from "../components/formatterGrids";

export function getColumns() {
  return [
    {
      field: "name",
      headerName: "Moedas",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: (params) => (
        <GridTitle title={params.value} />
      ),
    },
    {
      field: "qnt",
      headerName: "Quantidade",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: ({ row, value }) => {
        const formatted = formatQuantity(row.name, value);
        return (
          <GridRow formattedValue={formatted} />
        );
      }
    },
    {
      field: "value_invest",
      headerName: "Preço\nmédio",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: ({ row, value }) => {
        const formatted = formatCurrency(row.name, value);
        return (
          <GridRow formattedValue={formatted} />
        );
      },
    },
    {
      field: "price",
      headerName: "Preço\natual",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: ({ row, value }) => {
        const formatted = formatCurrency(row.name, value);
        return (
          <GridRow formattedValue={formatted} />
        );
      },
    },
    {
      field: "max_historica",
      headerName: "Máxima\nhistórica",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName} />
      ),
      renderCell: ({ row, value }) => {
        const formatted = formatCurrency(row.name, value);
        return (
          <GridRow formattedValue={formatted} />
        );
      },
    },
    {
      field: "spent",
      headerName: "Valor\nInvestido",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: ({ row, value }) => {
        const formatted = formatCurrency(row.name, value);
        return (
          <GridRow formattedValue={formatted} />
        );
      },
    },
    {
      field: "valor_atual",
      headerName: "Valor\nAtual",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName} />
      ),
      renderCell: ({ row, value }) => {
        const formatted = formatCurrency(row.name, value);
        return (
          <GridRow formattedValue={formatted} />
        );
      },
    },
    {
      field: "lucro",
      headerName: "Lucro",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: ({row, value}) => {
        const formatted = formatCurrencyLucro(row.name, value);
        return (
          <GridRowLucro formattedValue={formatted} value={value} />
        );
      },
    },
    {
      field: "percentual",
      headerName: "Lucro percentual",
      flex: 1,
      headerAlign: "center",
      align: "center",
      renderHeader: (params) => (
        <GridHeader title={params.colDef.headerName}/>
      ),
      renderCell: (params) => {
        const formatted = formatPercent(params.value);
        return (
          <GridRowLucro formattedValue={formatted} value={params.value} />
        );
      },
    },
  ];
}