function RegulonDBIgnorance

%Load all TF regulatory connections
[Dummy,TFInteractions]=xlsread('generegulation_tmp.xlsx');
%Determine the set of regulated genes
RegGenes=unique(TFInteractions(:,8));


%Find the positions of the these genes
[GenesNUM,GenesTXT]=xlsread('gene.xlsx');
GeneStart=min(GenesNUM(:,1:2)')';
GeneEnd=max(GenesNUM(:,1:2)')';


%Figure out which genes are regulated
RegGenesFilter=false(size(GenesTXT(:,2)));
for i=1:length(RegGenes)
    RegGenesFilter=RegGenesFilter+strcmp(GenesTXT(:,2),RegGenes(i));
end
RegGenesFilter=logical(RegGenesFilter);
RegGeneStart=GeneStart(RegGenesFilter);


%Load all operons
[OperonsNUM,OperonsTXT]=xlsread('operon.xlsx');
%Define the operon as the span of all genes and regulatory regions 
OperonLength=(max(OperonsNUM')-min(OperonsNUM'))';
OperonSpan=[min(OperonsNUM')',max(OperonsNUM')'];
OperonGeneSpan=[min(OperonsNUM(:,1:2)')',max(OperonsNUM(:,1:2)')'];



%Go through the list of operons and see if there's a regulated gene within
%it
OperonFilter=zeros(size(OperonLength));
for i=1:length(RegGeneStart)
    OperonFilter=OperonFilter+...
        double((OperonGeneSpan(:,1)<=RegGeneStart(i))&(OperonGeneSpan(:,2)>=RegGeneStart(i)));
end
OperonFilter=OperonFilter>0;



%% Make a plot of each regulated operon by painting all corresponding base pairs
GenomeLength=4639221;

GenomeRange=1:GenomeLength;
RegulatedBP=nan(size(GenomeRange));
NonRegulatedBP=nan(size(GenomeRange));

RegOperonSpan=[OperonSpan(OperonFilter,1),OperonSpan(OperonFilter,2)];
for i=1:length(RegOperonSpan)
    RegulatedBP(RegOperonSpan(i,1):RegOperonSpan(i,2))=1;
end


NonRegOperonSpan=[OperonSpan(~OperonFilter,1),OperonSpan(~OperonFilter,2)];
for i=1:length(RegOperonSpan)
    NonRegulatedBP(NonRegOperonSpan(i,1):NonRegOperonSpan(i,2))=1;
end



%Plot it in polar coordinates and add the lac operon as a reference

%Find the lac operon coordinate
lacIndex=find(strcmp(OperonsTXT(:,2),'lacZYA'));
%Find the mscL operon
mscLIndex=find(strcmp(OperonsTXT(:,2),'mscL'));
%oriC position
oriCPos=[3925744,3925975];


%Find the closest unregulated operon to lac
OperonSpanNoLac=OperonSpan;
OperonSpanNoLac(lacIndex,:)=inf;        %Remove lac
OperonSpanNoLac(OperonFilter,:)=inf;    %Remove all regulated operons

%Find the closest operons
[Dummy,Ind1]=min((OperonSpanNoLac(:,1)-OperonSpan(lacIndex,2)).^2);
[Dummy,Ind2]=min((OperonSpanNoLac(:,2)-OperonSpan(lacIndex,1)).^2);
%Who are they?
OperonsTXT(Ind1,:)
yaiLInd=Ind1;
OperonsTXT(Ind2,:)
yahOInd=Ind2;
%Are they regulated
OperonFilter(Ind1)
OperonFilter(Ind2)

%Start at oriC
StartCoordinate=mean(oriCPos)/GenomeLength*2*pi;

figure(1)
PlotHandle=polar(GenomeRange/GenomeLength*2*pi-StartCoordinate,RegulatedBP,'-b');
set(PlotHandle,'LineWidth',5)
hold on
PlotHandle(end+1)=polar(GenomeRange/GenomeLength*2*pi-StartCoordinate,NonRegulatedBP,'-r');
set(PlotHandle(end),'LineWidth',5)
PlotHandle(end+1)=polar(OperonSpan(lacIndex,:)/GenomeLength*2*pi-StartCoordinate,...
    ones(size(OperonSpan(lacIndex,:))),'-c');
set(PlotHandle(end),'LineWidth',15,'MarkerSize',25)
% PlotHandle(end+1)=polar(OperonSpan(mscLIndex,:)/GenomeLength*2*pi,...
%     ones(size(OperonSpan(mscLIndex,:))),'-k');
%set(PlotHandle(end),'LineWidth',15,'MarkerSize',25)
PlotHandle(end+1)=polar(oriCPos/GenomeLength*2*pi-StartCoordinate,...
    ones(size(oriCPos)),'.g');
set(PlotHandle(end),'LineWidth',15,'MarkerSize',25)
PlotHandle(end+1)=polar(OperonSpan(yaiLInd,:)/GenomeLength*2*pi-StartCoordinate,...
    ones(size(OperonSpan(yaiLInd,:))),'-m');
set(PlotHandle(end),'LineWidth',15,'MarkerSize',25)
% PlotHandle(end+1)=polar(OperonSpan(yahOInd,:)/GenomeLength*2*pi,...
%     ones(size(OperonSpan(yahOInd,:))),'-y');
% set(PlotHandle(end),'LineWidth',15,'MarkerSize',25)
hold off
legend('Regulated operons','Unregulated operons','lacZYA','oriC','yaiL',...
    'Location','SouthWestOutside')
xlim([-5,5])
get(gca)


%Distribution of lengths of regulated and unregulated operons

%Regulated and unregulated operons
[sum(OperonFilter),sum(~OperonFilter)]
%Mean length
[mean(OperonLength(OperonFilter)),mean(OperonLength(~OperonFilter))]


[RegCounts,Bins]=hist(OperonLength(OperonFilter),50);
UnregCounts=hist(OperonLength(~OperonFilter),Bins);
figure(2)
PlotHandle=bar(Bins,UnregCounts,'r');
hold on
PlotHandle(end+1)=bar(Bins,RegCounts,'b','Barwidth',0.5);
hold off
xlabel('length (bp)')
ylabel('number of operons')
legend('unregulated operons','regulated operons')
StandardFigurePBoC([],gca)


