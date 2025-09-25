import FinanceHeader from "../../../components/finance/FinanceHeader";
import KPIGrid from "../../../components/finance/KPIGrid";
import CostsPanel from "../../../components/finance/CostsPanel";
import RevenueChartCard from "../../../components/finance/RevenueChartCard";
import RulesPanel from "../../../components/finance/RulesPanel";
import { financeKpis } from "../../../data/finance/kpis";

export default function FinancePage() {
  return (
    <div className="max-w-[1200px] mx-auto">
      <FinanceHeader subtitle="Simplified P&L for paid media. Adjust time to update KPIs, costs, and charts." />
      <KPIGrid kpis={financeKpis} />
      <CostsPanel />
      <RevenueChartCard />
      <RulesPanel />
    </div>
  );
}
