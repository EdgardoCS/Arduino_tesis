test = {'t1','t1','t1','t1','t1','t1','t2','t2','t2','t2','t2','t1'};

%result = [];
for a = 1:13:180
    a
    score = [];
    for b = a
        score = [score,VAS(b)]
        if length(score) == 12
            p = kruskalwallis(score,test,'off');
            disp(p);
            %result = [result,p];
            score = [];
        end
    end
end

%p = kruskalwallis(vas15,test,'off');
